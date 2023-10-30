from reactpy import component, html
from components import nabvar_side, footer, navbar_user
from reactpy_router import link
import pyodbc

SERVER = 't2sqlsv.database.windows.net'
DATABASE = 't2sql'
USERNAME = 'tier2'
PASSWORD = 'mdr-xd100'
connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'
cnxn = pyodbc.connect(connectionString)
cursor = cnxn.cursor()
cursor.execute("CREATE TABLE t2sql.dbo.TIPOS_ALMACEN (ID_TIPO numeric(2,0),NOMBRE_TIPO varchar(25))")
cursor.execute("INSERT INTO t2sql.dbo.TIPOS_ALMACEN (ID_TIPO,NOMBRE_TIPO) VALUES(1,'PROD TERM')")
cursor.execute("INSERT INTO t2sql.dbo.TIPOS_ALMACEN (ID_TIPO,NOMBRE_TIPO) VALUES(2,'MP')")
cursor = cnxn.cursor()
cursor.execute("COMMIT")
cursor.execute("SELECT * FROM t2sql.dbo.TIPOS_ALMACEN")
result =""
row = cursor.fetchone() 
while row:
    print (row)
    result += str(row);
    row = cursor.fetchone()
@component
def error():
    bootstrap_css = html.link({
        "rel": "stylesheet",
        "href": "https://elpatronhh.github.io/portfolio/bootstrap.min.css"
    })
    style_css = html.link({
            "href": "https://elpatronhh.github.io/portfolio/sb-admin-2.min.css",
            "rel": "stylesheet"
        })
    fontawesome = html.link({
            "href": "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css",
            "rel": "stylesheet",
        })
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
            html.div( {"id":"page-top"},
                     html.div({"id":"wrapper"},          
                              html.ul({"class":"navbar-nav bg-gradient-primary sidebar sidebar-dark accordion","id":"accordionSidebar"},
                                       html.a(link(html.div({"class":"sidebar-brand-icon rotate-n-15"},
                                                                 html.i({"class":"fas fa-laugh-wink"})
                                                        ),
                                                        html.div({"class":"sidebar-brand-text mx-3"},
                                                                 "SB ADMIN", html.sup("2")),
                                                        to="/login",**{"class":"sidebar-brand d-flex align-items-center justify-content-center"}),
                                                        ),
                                                        html.hr({"class":"sidebar-divider my-0"}),
                                                        html.div({"class":"sidebar-heading"},"Addons"),
                                                        html.li({"class":"nav-item active"},
                                                                html.a({"class":"nav-link", "href":"#", "data-toggle":"collapse", "data-target":"#collapsePages", "aria-expanded":"true", "aria-controls":"collapsePages"},
                                                                       html.i({"class":"fas fa-fw fa-folder"}),
                                                                       html.span("Pages")),
                                                                       html.div({"id":"collapsePages", "class":"collapse show", "aria-labelledby":"headingPages", "data-parent":"#accordionSidebar"},
                                                                           html.div({"class":"bg-white py-2 collapse-inner rounded"},
                                                                                    html.h6({ "class":"collapse-header"},"Login Screens"),
                                                                                    html.a(link("login", to="/login",**{"class":"collapse-item"}))
                                                                                    
                                                                                    )     
                                                                           
                                                                       )
                                                        ),
                                            ),
                                            html.div({"class":"container-fluid"},
                                                html.div({"class":"text-center"},
                                                     html.div({ "class":"error mx-auto", "data-text":"404"},"404"),
                                                     html.p({"class":"lead text-gray-800 mb-5"},"Page Not Found"),
                                                     html.p({"class":"text-gray-500 mb-0"},"It looks like you found a glitch in the matrix.. Lorem Ipsum Dolor Amet")
                                                     )),
                                    ),
                            footer.footer(),            

                    ),
            html.script({"src":"https://elpatronhh.github.io/portfolio/startbootstrap-sb-admin-2-gh-pages/vendor/jquery/jquery.min.js"}),
            html.script({"src":"https://elpatronhh.github.io/portfolio/startbootstrap-sb-admin-2-gh-pages/vendor/bootstrap/js/bootstrap.bundle.min.js"}),
            html.script({"src":"https://elpatronhh.github.io/portfolio/startbootstrap-sb-admin-2-gh-pages/vendor/jquery-easing/jquery.easing.min.js"}),
            html.script({"src":"https://elpatronhh.github.io/portfolio/startbootstrap-sb-admin-2-gh-pages/js/sb-admin-2.min.js"}),
            html.script({"src":"https://elpatronhh.github.io/portfolio/startbootstrap-sb-admin-2-gh-pages/vendor/chart.js/Chart.min.js"}),
            html.script({"src":"https://elpatronhh.github.io/portfolio/startbootstrap-sb-admin-2-gh-pages/js/demo/chart-area-demo.js"}),
            html.script({"src":"https://elpatronhh.github.io/portfolio/startbootstrap-sb-admin-2-gh-pages/js/demo/chart-pie-demo.js"}),
            html.script({"src":"https://cdn.jsdelivr.net/npm/bootstrap@4.1.3/dist/js/bootstrap.bundle.min.js"})


        )

        
    )
