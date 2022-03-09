r1 = fluidRow(column(12,h1("Algorand Price"), align = "center"))
r2 = fluidRow(column(12, plotOutput("plot")))
ui = fluidPage(r1, r2)
