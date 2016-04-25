type = ['','info','success','warning','danger'];

countdate = document.getElementById("countdate").value;
countdate = countdate.split(",");

demo = {
    initPickColor: function(){
        $('.pick-class-label').click(function(){
            var new_class = $(this).attr('new-class');  
            var old_class = $('#display-buttons').attr('data-class');
            var display_div = $('#display-buttons');
            if(display_div.length) {
            var display_buttons = display_div.find('.btn');
            display_buttons.removeClass(old_class);
            display_buttons.addClass(new_class);
            display_div.attr('data-class', new_class);
            }
        });
    },
    
    initChartist: function(){    
        
      
        
        
        
        
    
        var data = {
          labels: ['20th feb', '22 Feb', '23 feb', '24 feb', '25 feb', '26 feb', '27 feb'],
          series: [ countdate]
        };
     

        var options = {
            seriesBarDistance: 10,
            axisX: {
                showGrid: false
            },
            height: "245px"
        };
        
        var responsiveOptions = [
          ['screen and (max-width: 640px)', {
            seriesBarDistance: 5,
            axisX: {
              labelInterpolationFnc: function (value) {
                return value[0];
              }
            }
          }]
        ];
        
        Chartist.Bar('#chartActivity', data, options, responsiveOptions);
    
        var dataPreferences = {
            series: [
                [25, 30, 20, 25]
            ]
        };
        
        var optionsPreferences = {
            donut: true,
            donutWidth: 40,
            startAngle: 0,
            total: 100,
            showLabel: false,
            axisX: {
                showGrid: false
            }
        };
    
        Chartist.Pie('#chartPreferences', dataPreferences, optionsPreferences);
         
	var obj = [8, 8,8,8,8,]
        Chartist.Pie('#chartPreferences', {
          labels: ['male', 'female'],
          series: a123
        });  
    },
    
  
    
	

    
}

