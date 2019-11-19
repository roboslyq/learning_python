# encoding: utf-8
import os
import json
import sys
from urllib.parse import urljoin
import pdfkit
from com.roboslyq.python.learn.spider.geektime.cfg import options
from com.roboslyq.python.learn.spider.geektime.common import post, log, base_url, error_articles, create_dir, login, \
    init, pdf_options, path_wk
from com.roboslyq.python.learn.spider.geektime.models import Product, Article
from PyPDF2 import PdfFileMerger  # pdf 合并工具包


def get_all_products(product_array):
    """
    获取已购买的所有产品(专栏)
    TODO: 极客时间对my/products/all做了分页，当前只实现了第一页的数据获取
    :return: 专栏id和专栏标题的字典
    """
    if product_array is not None:
        return product_array  # 表示指定了下载内容，直接返回
    else:
        response = post(urljoin(base_url, 'my/products/all'))
        data = response.json(encoding='utf-8')['data']
        if len(data) == 0 or len(data[0]['list']) == 0:
            raise Exception("没有购买的专栏")
        log.info("get products success")
        return [Product(d['extra']['column_id'], d['title']) for d in data[0]['list']]


def get_all_products_callback(products):
    """
    对爬取的产品进行处理的回调(这里并没有使用异步线程池, 主动调用的)
    :param products: get_all_products返回的产品字典
    :return:
    """
    for product in products:
        get_all_articles_callback(get_all_articles(product), product)


def get_all_articles(product):
    """
    获取专栏下的所有文章
    :param product: 单个产品(专栏)
    :return: 文章id和文章标题的字典
    """
    payload = {
        "cid": product.id,
        "size": 500,
        "prev": 0,
        "order": "earliest",
        "sample": False
    }
    response = post(urljoin(base_url, 'column/articles'), payload)
    log.info("gat all articles success for product(id=%s, title=%s)" % (product.id, product.title))
    data = response.json(encoding='utf-8')['data']
    return [Article(str(d['id']), d['article_title']) for d in data['list']]


def get_all_articles_callback(articles, product):
    """
    对爬取的文章进行处理的回调(这里并没有使用异步线程池, 主动调用的)
    :param articles: get_all_articles返回的文章字典
    :param product: 文章所属于的产品(专栏)
    :return:
    """

    path = options.save_dir
    product_path = os.path.join(path, str(product.id))
    create_dir(product_path)

    pdf_list = []  # pdf文件，供关闭文件流时使用
    pdf_tag = []  # pdf页签
    for article in articles:
        title = article.title.replace(' ', '_').replace('|', '').replace('：', '').replace('?', '').replace('（', '') \
            .replace('）', '').replace('/', '').replace('*', '').replace('?', '').replace('？', '')
        article_path = os.path.join(
            product_path,
            article.id
        )
        # title中包含中文字符,会导致Pdf写文件失败,所以此处只保存id作为临时文件名称
        # '{}_{}.pdf'.format(article.id, title))
        article_id_path = os.path.join(product_path, '{}.pdf'.format(article.id))
        # 保存文件到list中，合并时使用
        pdf_list.append(article_id_path)
        if article.title is not None:  # (如果title包含有中文或者特殊字符，会导致写pdf失败。)
            pdf_tag.append(article.title)
        else:
            pdf_tag.append(article_id_path)
        # 检查是否曾经下载过，如果曾经下载载则直接返回
        if os.path.exists(article_path) or os.path.exists(article_id_path):
            continue
        try:
            content = get_article_content(article)
            article.content = content
        except Exception as e:
            log.error(str(e))
            error_articles.append(article)
            continue
        write_pdf(article, article_path, article_id_path)
    # 合并PDF
    merge_pdf(product_path, pdf_list, pdf_tag)


def write_pdf(article, article_path, article_id_path):
    """
    将文章内容写入本地pdf文件中, 首次尝试以文章标题为文件名, 若写入失败(标题中有特殊字符), 则使用文章id为文件名
    :param article: 要写入的文章
    :param article_path: 以标题命名的文章绝对路径
    :param article_id_path: 以id命名的文章绝对路径
    :return:
    """
    try:
        log.info('write %s' % article_path)
        config = pdfkit.configuration(wkhtmltopdf=path_wk)
        pdfkit.from_string(article.content, article_id_path, options=pdf_options, configuration=config)
    except OSError:
        try:
            log.info('write %s' % article_id_path)
            pdfkit.from_string(article.content, article_id_path)
        except Exception as e:
            log.error(str(e))
            error_articles.append(article)
    except Exception as e:
        log.error(str(e))
        error_articles.append(article)


def merge_pdf(product_path, pdf_list, pdf_tag):
    """
    合并PDF
    :param pdf_list:  pdf集合
    :param product_path:
    :param pdf_tag: 与每个pdf对应的页签
    :return:
    """
    #  合并
    merger = PdfFileMerger()
    pdf_open_list = []
    i = 0
    for pdf in pdf_list:
        # with open(download_file_path + pdf, 'rb') as f:
        #     merger.append(f)
        #     print(u"合并完成第" + str(i) + '个pdf' + pdf)
        print(u"合并第" + str(i) + '个pdf' + pdf + "开始")
        tagi = pdf_tag[i]
        f = open(pdf, 'rb')
        # merger.append(file_rd, bookmark=short_filename, import_bookmarks=import_bookmarks)
        pdf_open_list.append(f)
        merger.append(f, bookmark=tagi, import_bookmarks=True)
        # 此处不能关闭，会导致结果文件为空
        # f.close()
        print(u"合并完成第" + str(i) + '个pdf' + pdf)
        i = i + 1
    output = open(os.path.join(product_path, '{}.pdf'.format('merged_all')), "wb")
    merger.write(output)
    merger.close()
    # TODO 关闭相关文件


def get_article_content(article):
    """
    获取文章内容
    :param article: 目标文章
    :return: 文章内容的html
    """
    payload = {
        "id": article.id,
        "include_neighbors": False,
        "is_freelyread": False
    }
    log.info("prepare to get article(%s)" % article)
    response = post(urljoin(base_url, 'article'), payload)
    log.info("gat article success for article(id=%s, title=%s)" % (article.id, article.title))
    data = response.json(encoding='utf-8')['data']
    html_title = '<center><h1>' + article.title + '<h1></center>'
    if 'article_content' not in data:
        raise Exception("no article content, data is: %s" % json.dumps(data, indent=4))
    return '<meta charset="utf-8">' + html_title + data['article_content']


def main():
    """
    主函数
    :return:
    """
    init()
    # 若product_array空时，表示全部下载。
    product_array = [Product('126', '数据结构与算法之美')]
    log.info("start--------------")
    try:
        login(options.cell_phone, options.password)
        get_all_products_callback(get_all_products(product_array))
    except KeyboardInterrupt:
        log.info("exit...")
    except Exception as e:
        log.error(e)
        sys.exit(1)
    if len(error_articles) > 0:
        log.error("%d article save error, please retry" % len(error_articles))
    else:
        log.info("save success")


if __name__ == '__main__':
    main()
