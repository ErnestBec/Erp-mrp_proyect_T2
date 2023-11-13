from reactpy import component, html
from reactpy_router import link

#
@component
def shopping():
    bootstrap_css = html.link({
        "rel": "stylesheet",
        "href": "https://elpatronhh.github.io/portfolio/bootstrap.min.css"
    }),
    style_css = html.link({
        "href": "https://elpatronhh.github.io/portfolio/sb-admin-2.min.css",
        "rel": "stylesheet"
    }),
    fontawesome = html.link({
        "href": "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css",
        "rel": "stylesheet",
    }),
    head = html.div(
        html.meta({
            "charset": "utf-8"
        }),
        html.meta({
            "http-equiv": "X-UA-Compatible",
            "content": "IE=edge"
        }),
        html.meta({
            "name": "viewport",
            "content": "width=device-width, initial-scale=1, shrink-to-fit=no"
        }),
        html.meta({
            "name": "description",
            "content": ""
        }),
        html.meta({
            "name": "author",
            "content": ""
        }),
        html.title("PANEL ADMINISTRADOR"),
        html.link({
            "href": "https://fonts.googleapis.com/css?family=Nunito:200,200i,300,300i,400,400i,600,600i,700,700i,800,800i,900,900i",
            "rel": "stylesheet"
        }),

    ),

    return (
        html.div(
            bootstrap_css,
            style_css,
            fontawesome,
            head,
            html.div(
                link("Dashboard", to="/")
            ),
            html.script(
                {"src": "https://elpatronhh.github.io/portfolio/startbootstrap-sb-admin-2-gh-pages/vendor/jquery/jquery.min.js"}),
            html.script(
                {"src": "https://elpatronhh.github.io/portfolio/startbootstrap-sb-admin-2-gh-pages/vendor/bootstrap/js/bootstrap.bundle.min.js"}),
            html.script(
                {"src": "https://elpatronhh.github.io/portfolio/startbootstrap-sb-admin-2-gh-pages/vendor/jquery-easing/jquery.easing.min.js"}),
            html.script(
                {"src": "https://elpatronhh.github.io/portfolio/startbootstrap-sb-admin-2-gh-pages/js/sb-admin-2.min.js"}),
            html.script(
                {"src": "https://elpatronhh.github.io/portfolio/startbootstrap-sb-admin-2-gh-pages/vendor/chart.js/Chart.min.js"}),
            html.script(
                {"src": "https://elpatronhh.github.io/portfolio/startbootstrap-sb-admin-2-gh-pages/js/demo/chart-area-demo.js"}),
            html.script(
                {"src": "https://elpatronhh.github.io/portfolio/startbootstrap-sb-admin-2-gh-pages/js/demo/chart-pie-demo.js"}),
            html.script(
                {"src": "https://cdn.jsdelivr.net/npm/bootstrap@4.1.3/dist/js/bootstrap.bundle.min.js"})
        )
    )
