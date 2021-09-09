import csv
import math
from django.shortcuts import render
#from django.views.generic import TemplateView
# from django.templatetags.static import static
from django.core.paginator import Paginator


# Create your views here.

def index(request):
    PRODUCTS_PER_PAGE = 24
    with open('store/darazfull.csv', encoding='utf-8') as products_file:
        file_reader = csv.reader(products_file, delimiter=',')
        products_list = list(file_reader)
        products_list = products_list[1:]
        products_count = len(products_list)
        pages_count = math.ceil(products_count / PRODUCTS_PER_PAGE)
        short_list = products_list[0:24]
        print(pages_count)
    return render(request, 'store/home.html', context={'short_product_list': short_list, 
        'pages_count': pages_count, 'pages_range':  range(0, pages_count, 1)})

def products_by_page(request, page_number):
    PRODUCTS_PER_PAGE = 24
    with open('store/darazfull.csv', encoding='utf-8') as products_file:
        file_reader = csv.reader(products_file, delimiter=',')
        products_list = list(file_reader)
        products_list = products_list[1:]

        products_count = len(products_list)
        pages_count = math.ceil(products_count / PRODUCTS_PER_PAGE)
        # short_list = products_list[0:24]

        start_list = PRODUCTS_PER_PAGE * page_number - PRODUCTS_PER_PAGE
        end_list = PRODUCTS_PER_PAGE * page_number

        short_list = products_list[start_list:end_list]
    return render(request, 'store/home.html', context={'short_product_list': short_list,
        'pages_count': pages_count, 'pages_range': range(0, pages_count, 1)})

def products_by_page_Search(request, page_number):
    PRODUCTS_PER_PAGE = 24
    with open('store/darazfull.csv', encoding='utf-8') as products_file:
        file_reader = csv.reader(products_file, delimiter=',')
        products_list = list(file_reader)
        products_list = products_list[1:]
        products_count = len(products_list)
        pages_count = math.ceil(products_count / PRODUCTS_PER_PAGE)
        # short_list = products_list[0:24]

        start_list = PRODUCTS_PER_PAGE * page_number - PRODUCTS_PER_PAGE
        end_list = PRODUCTS_PER_PAGE * page_number

        short_list = products_list[start_list:end_list]
    return render(request, 'store/search.html', context={'short_product_list': short_list,
        'pages_count': pages_count, 'pages_range': range(0, pages_count, 1)})

    
def products_search(request, q):
    PRODUCTS_PER_PAGE = 24
    with open('store/darazfull.csv', encoding='utf-8') as products_file:
        file_reader = csv.reader(products_file, delimiter=',')
        products_list = list(file_reader)
        products_list = products_list[1:]
        products_list = list(filter(lambda product: q.lower() in product[0][:40].lower(), products_list))

        products_list = sorted(sorted(products_list, key=sortByRs), key=sortByRating, reverse=True)
        products_count = len(products_list)
        pages_count = math.ceil(products_count / PRODUCTS_PER_PAGE)

    return render(request, 'store/search.html', context={'short_product_list': products_list})

def sortByRs(product):
    strPrice = product[6]
    strPrice = strPrice[4:]
    priceList = strPrice.split(',')
    price = int(''.join(priceList))
    print(price)
    return price


def sortByRating(product):
    strRating = product[7]
    strRating = strRating[0:]
    ratinglist = strRating.split(',')
    rating = float(''.join(ratinglist))
    return rating
