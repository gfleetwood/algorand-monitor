shinyServer(function(input, output, session) {
  
  get_data = function(){
    
    con %>% 
      tbl("algorand_price_data") %>%
      collect()
    
  }
  
  data = reactivePoll(1000, session, (function(x) FALSE), get_data) 
  
  output$plot <- renderPlot({
    ggplot(data(), aes(created_at, price)) + geom_line()
  })

})
