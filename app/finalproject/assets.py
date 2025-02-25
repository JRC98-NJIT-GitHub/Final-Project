"""Compile static assets."""
from flask import current_app as app
from flask_assets import Bundle


def compile_static_assets(assets):
    """Configure and build asset bundles."""
    main_js_bundle = Bundle(
        'src/js/main.js',
        filters='jsmin',
        output='dist/js/main.min.js'
    )  # Main JavaScript Bundle
    assets.register('main_js', main_js_bundle)
    main_js_bundle.build()
    return assets
