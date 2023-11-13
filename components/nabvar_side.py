from reactpy import component, html
from reactpy_router import link

#
@component
def navbar():
    return (

        # sidebar
        html.ul({
            "class": "navbar-nav bg-gradient-primary sidebar sidebar-dark accordion",
                     "id": "accordionSidebar"
        },
            # Sidebar - Brand
            html.a({
                "class": "sidebar-brand d-flex align-items-center justify-content-center",
                         "href": "/"
            },
            html.div({
                "class": "sidebar-brand-icon rotate-n-15"
            },
                html.i({
                    "class": "fas fa-laugh-wink"
                })
            ),
            html.div({
                "class": "sidebar-brand-text mx-3"
            },
                "ADMINISTRADOR",
                html.sup()
            )
        ),


            # Divider
            html.hr({
                "class": "sidebar-divider my-0"
            }),

            # Nav Item - Dashboard
            html.li({
                "class": "nav-item active"
            },
            html.a({
                "class": "nav-link",
                "href": "index.html"
            },
                html.i({
                       "class": "fas fa-fw fa-tachometer-alt"
                       }),
                "Dashboard"
            )
        ),

            # Divider
            html.hr({
                "class": "sidebar-divider"
            }),

            # Heading - Interface
            html.div({
                "class": "sidebar-heading"
            },
            "Interface"
        ),

            # Nav Item - Pages Collapse Menu (TIER1)
            html.li({"class": "nav-item"},
                    html.a({"class": "nav-link collapsed",
                                     "href": "#",
                                     "data-toggle": "collapse",
                                     "data-target": "#collapseTwo",
                                     "aria-expanded": "true",
                                     "aria-controls": "collapseTwo"
                            },
                           html.i({"class": "fas fa-fw fa-cog"}),
                           "TIER1"
                           ),
                    html.div({"class": "collapse",
                                       "id": "collapseTwo",
                                       "aria-labelledby": "headingTwo",
                                       "data-parent": "#accordionSidebar"},
                             html.div({"class": "bg-white py-2 collapse-inner rounded"},
                                      html.h6({
                                          "class": "collapse-header"
                                      },
                                 "Custom Components:"
                             ),
                        link("Compra", to="/shopping", **{
                                          "class": "collapse-item",
                                          "href": "buttons.html"
                        }),
                        html.a({
                            "class": "collapse-item",
                            "href": "cards.html"
                        },
                                 "Pedidos"
                             )
                    )
            )
        ),

            # Nav Item - Pages Collapse Menu (TIER2)
            html.li({
                "class": "nav-item"
            },
            html.a({
                "class": "nav-link collapsed",
                "href": "#",
                "data-toggle": "collapse",
                "data-target": "#collapseUtilities",
                "aria-expanded": "true",
                "aria-controls": "collapseUtilities"
            },
                html.i({
                       "class": "fas fa-fw fa-wrench"
                       }),
                "TIER2"
            ),
            html.div({
                "class": "collapse",
                "id": "collapseUtilities",
                "aria-labelledby": "headingUtilities",
                "data-parent": "#accordionSidebar"
            },
                html.div({
                         "class": "bg-white py-2 collapse-inner rounded"
                         },
                         html.h6({
                             "class": "collapse-header"
                         },
                    "Custom Utilities:"
                ),
                html.a({
                    "class": "collapse-item",
                    "href": "utilities-color.html"
                },
                    "Colors"
                ),
                html.a({
                    "class": "collapse-item",
                    "href": "utilities-border.html"
                },
                    "Borders"
                ),
                html.a({
                    "class": "collapse-item",
                    "href": "utilities-animation.html"
                },
                    "Animations"
                ),
                link("Other", to="/utilothers", **{
                    "class": "collapse-item",
                    "href": "utilities-other.html"
                }

                )
            )
            )
        ),

            # Nav Item - Pages Collapse Menu (TIER3)
            html.li({
                "class": "nav-item"
            },
            html.a({
                "class": "nav-link collapsed",
                "href": "#",
                "data-toggle": "collapse",
                "data-target": "#collapseTIER3"
            },
                html.i({
                       "class": "fas fa-fw fa-cog"
                       }),
                "TIER3"
            ),
            html.div({
                "class": "collapse",
                "id": "collapseTIER3",
                "aria-labelledby": "headingTwo",
                "data-parent": "#accordionSidebar"
            },
                html.div({
                         "class": "bg-white py-2 collapse-inner rounded"
                         },
                         html.h6({
                             "class": "collapse-header"
                         },
                    "Custom Components:"
                ),
                html.a({
                    "class": "collapse-item",
                    "href": "buttons.html"
                },
                    "Buttons"
                ),
                html.a({
                    "class": "collapse-item",
                    "href": "cards.html"
                },
                    "Cards"
                )
            )
            )
        ),

            # Nav Item - Pages Collapse Menu (LOGISTICA)
            html.li({
                "class": "nav-item"
            },
            html.a({
                "class": "nav-link collapsed",
                "href": "#",
                "data-toggle": "collapse",
                "data-target": "#collapseLOGISTICA"
            },
                html.i({
                       "class": "fas fa-fw fa-cog"
                       }),
                "LOGISTICA"
            ),
            html.div({
                "class": "collapse",
                "id": "collapseLOGISTICA",
                "aria-labelledby": "headingTwo",
                "data-parent": "#accordionSidebar"
            },
                html.div({
                         "class": "bg-white py-2 collapse-inner rounded"
                         },
                         html.h6({
                             "class": "collapse-header"
                         },
                    "Custom Components:"
                ),
                html.a({
                    "class": "collapse-item",
                    "href": "buttons.html"
                },
                    "Buttons"
                ),
                html.a({
                    "class": "collapse-item",
                    "href": "cards.html"
                },
                    "Cards"
                )
            )
            )
        ),

            # Divider
            html.hr({
                "class": "sidebar-divider"
            }),

            # Heading - Addons
            html.div({
                "class": "sidebar-heading"
            },
            "Addons"
        )
        )

    )
