def product_image_upload(instance, filename):
    return 'product_{0}/{1}'.format(instance.id, filename)