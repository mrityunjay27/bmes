from bmes.cataloguebp import views, models, catalogue_service

@views.catalogue.context_processor
def inject_context():
    """
    This data will be exposed within this context. All templates, all files will have access,
    basically in catalogue blueprint
    :return:
    """
    return {
              'categories': models.Category.query.filter_by(category_status= models.StatusType.Active).all(),
              'brands': models.Brand.query.filter_by(brand_status=models.StatusType.Active).all(),
              'selected_category':'all-categories',
              'selected_brand':'all-brands',
           }