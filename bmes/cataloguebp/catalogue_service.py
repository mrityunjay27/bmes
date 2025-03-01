from bmes.cataloguebp.models import Brand, Category, StatusType, Product


def fetch_products(request, category_slug, brand_slug):
    """
    Utility method to fetch product and does filtering if asked.
    :param request:
    :param category_slug:
    :param brand_slug:
    :return:
    """
    page = int(request.args.get('page', 1))

    page_object = None

    # Filter the products
    if category_slug == 'all-categories' and brand_slug == 'all-brands':
        page_object = Product.query.filter_by(product_status=StatusType.Active).paginate(page, 9, False)

    if category_slug != 'all-categories' and brand_slug != 'all-brands':
        page_object = (Product.query.filter_by(product_status=StatusType.Active)
                       .filter(Product.categories.any(Category.slug == category_slug))
                       .filter(Product.brands.any(Brand.slug == brand_slug)).paginate(page, 9, False)
                       )
    if category_slug != 'all-categories' and brand_slug == 'all-brands':
        page_object = (Product.query.filter_by(product_status=StatusType.Active)
                       .filter(Product.categories.any(Category.slug == category_slug)).paginate(page, 9, False)
                       )
    if category_slug == 'all-categories' and brand_slug != 'all-brands':
        page_object = (Product.query.filter_by(product_status=StatusType.Active)
                       .filter(Product.brands.any(Brand.slug == brand_slug)).paginate(page, 9, False)
                       )

    return page_object

# The page_object has the following properties and methods:
# items, pages, prev_num, next_num, iter_pages(), page, has_next, has_prev


def fetch_products_V2(request, category_slug, brand_slug):
    """
    Utility method to fetch products and apply filtering if requested.
    """
    page = int(request.args.get('page', 1))

    query = Product.query.filter_by(product_status=StatusType.Active)

    if category_slug != 'all-categories':
        query = query.filter(Product.categories.any(Category.slug == category_slug))

    if brand_slug != 'all-brands':
        query = query.filter(Product.brands.any(Brand.slug == brand_slug))

    """
    Query Execution
    The query gets built dynamically based on the filters.
    When .paginate(page, 9, False) is called, SQLAlchemy executes a LIMIT and OFFSET query behind the scenes.
    
    Pagination Mechanism
    If page = 1, it retrieves products 1-9 (LIMIT 9 OFFSET 0).
    If page = 2, it retrieves products 10-18 (LIMIT 9 OFFSET 9).
    If page = 3, it retrieves products 19-27 (LIMIT 9 OFFSET 18).
    """

    return query.paginate(page=page, per_page=9, error_out=False)
