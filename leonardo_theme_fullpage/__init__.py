try:
    from local_settings import APPS
except ImportError:
    pass

if 'leonardo_theme_fullpage' in APPS:
    LEONARDO_APPS = [
        'leonardo_theme_fullpage',
        'leonardo_module_analytics'
    ]

    LEONARDO_JS_FILES = [
        'js/mm.Angular-FullPage.min.js',
    ]

    LEONARDO_CSS_FILES = [
        'css/mm.angular-fullpage.css',
    ]

    LEONARDO_SCSS_FILES = []

    LEONARDO_CONFIG = {
        'SECTIONS_COLORS': ('#ff #f26f21', 'Color of sections'),
    }