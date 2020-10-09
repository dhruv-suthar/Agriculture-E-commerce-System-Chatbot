 $(document).ready(function()
  {
     all_url=window.location.href  ;
     all_url1=window.location.href;
     var p_cat_val='';
     var p_sort_val = '';
     var send_filter_data='';
     var p_min_val=0;
     var p_max_val=0;
     $('.largenav li:nth-child(2)').addClass("active");
  
       $('.sm-icon-wishlist').click(function(elem)
       {
       
         elem.preventDefault();

        

            if("{{session.logged_in}}")
            {

               

                
                 
                      $(this).toggleClass('glyphicon-heart glyphicon-heart-empty');
             if($(this).is('.glyphicon-heart'))
             {

                 $.ajax({
                url:'/user-wishlists/add',
                data:
                {

                  'add_wishlist_product_id':$(this).attr('id')
                },
                   success: function (response) {
                    //location.reload()
                   }
                  }); 

                   $.notify({
                    allow_dismiss: false,
                  icon: 'fa fa-check',
                  message: 'Successfully added to wishlist.',
                  placement: {
                    from: 'bottom',
                    align: 'center'
                }
                 
                },{
                  type: 'success'
                });


            }
            else
            {

                    $.ajax({
                  url:'/user-wishlists',
                  data:
                  {

                    'delete_wishlist_id':$(this).attr('id')
                  },
                     success: function (response) {
                      location.reload()
                     }
                    }); 


                   $.notify({
                    allow_dismiss: false,
                  icon: 'fa fa-check',
                  message: 'Successfully remove from wishlist.',
                 
                },{
                  type: 'danger'
                });


            }
                   

              
          
        }
        else
        {
         

       
                $.notify({
                  allow_dismiss: false,
                  icon: 'fa fa-times',
                  message: 'You have to login for add to wishlist',
                  placement: {
                from: 'bottom',
                align: 'left'
                }
                 
                },  
                 {
                  type: 'danger'
                }); 
         }

           

         
       });

         $('.sm-icon-compare').click(function(elem)
       {
         elem.preventDefault();

             $(this).toggleClass('glyphicon-random1 glyphicon-random-empty');
           if($(this).is('.glyphicon-random-empty'))
           {

             $.notify({
              allow_dismiss: false,
            icon: 'fa fa-check',
            message: 'Successfully remove from compare.',
             placement: {
                from: 'bottom',
                align: 'center'
          }
           
          },{
            type: 'success'
          });
          }
          else if($(this).is('.glyphicon-random1'))
          {

             $.notify({
              allow_dismiss: false,
            icon: 'fa fa-check',
            message: 'Successfully added from compare.',
            placement: {
                from: 'bottom',
                align: 'center'
          }
           
          },{
            type: 'success'
          });
          } 
           
         
       });

      
          $('#sort_by').change(function(event)
         {
            sort_data = $(this).val();
            get_cat_val= $('#product_category').val();
            get_sender_filter_data= send_filter_data;
            p_min_val=$('.js-input-from').val();
            p_max_val=$('.js-input-from').val()
            event.preventDefault();

            if(get_sender_filter_data && sort_data && get_cat_val ) 
            {
            $.ajax({
              url:'/products',
              data:
              {
                'filter_data':get_sender_filter_data,
                'p_sort':sort_data,
                'p_cat':get_cat_val
              },
                 success: function (response) {
                 
                      
                     //$(".product_show_area").html($(response).find(".product_show_area"));
                      $(".product_show_area").html($(response).find(".product_show_area"));
                     
              
                 
              }
            });
             if (history.pushState) {
                  history.pushState(null, null, location.pathname + '?filter_data=' + get_sender_filter_data + '&p_sort=' + sort_data + '&p_cat=' + get_cat_val );
              }

          }
          else if(get_sender_filter_data && sort_data)
          {
            $.ajax({
              url:'/products',
              data:
              {
                'filter_data':get_sender_filter_data,
                'p_sort':sort_data
              },
                 success: function (response) {
                 
                      
                     //$(".product_show_area").html($(response).find(".product_show_area"));
                      $(".product_show_area").html($(response).find(".product_show_area"));
                     
              
                 
              }
            });
             if (history.pushState) {
                  history.pushState(null, null, location.pathname + '?filter_data=' + get_sender_filter_data + '&p_sort=' + sort_data  );
              }

          }
          else if(sort_data && get_cat_val)
          {
             $.ajax({
              url:'/products',
              data:
              {
                'p_sort':sort_data,
                'p_cat':get_cat_val
              },
                 success: function (response) {
                 
                      
                     //$(".product_show_area").html($(response).find(".product_show_area"));
                      $(".product_show_area").html($(response).find(".product_show_area"));
                     
              
                 
              }
            });
              if (history.pushState) {
                  history.pushState(null, null, location.pathname + '?' + 'p_sort=' + sort_data + '&p_cat=' + get_cat_val );
              }
          }
          else if(sort_data)
          {
             $.ajax({
              url:'/products',
              data:
              {
                'p_sort':sort_data
              },
                 success: function (response) {
                 
                      
                     //$(".product_show_area").html($(response).find(".product_show_area"));
                      $(".product_show_area").html($(response).find(".product_show_area"));
                     
              
                 
              }
            });
              if (history.pushState) {
                  history.pushState(null, null, location.pathname + '?' +  'p_sort=' + sort_data  );
              }
          }    
         });
            $('#product_category').change(function(event)
         {
            sort_data =$('#sort_by').val();
            get_cat_val=$(this).val();
            get_sender_filter_data= send_filter_data;



            event.preventDefault();

            if(get_sender_filter_data && sort_data && get_cat_val) 
            {
            $.ajax({
              url:'/products',
              data:
              {
                'filter_data':get_sender_filter_data,
                'p_sort':sort_data,
                'p_cat':get_cat_val
              },
                 success: function (response) {
                 
                      
                     //$(".product_show_area").html($(response).find(".product_show_area"));
                      $(".product_show_area").html($(response).find(".product_show_area"));
                     
              
                 
              }
            });
             if (history.pushState) {
                  history.pushState(null, null, location.pathname + '?filter_data=' + get_sender_filter_data + '&p_sort=' + sort_data + '&p_cat=' + get_cat_val );
              }


          }
          else if(get_sender_filter_data && get_cat_val)
          {
            $.ajax({
              url:'/products',
              data:
              {
                'filter_data':get_sender_filter_data,
                'p_cat':get_cat_val
              },
                 success: function (response) {
                 
                      
                     //$(".product_show_area").html($(response).find(".product_show_area"));
                      $(".product_show_area").html($(response).find(".product_show_area"));
                     
              
                 
              }
            });
             if (history.pushState) {
                  history.pushState(null, null, location.pathname + '?filter_data=' + get_sender_filter_data + '&p_cat=' + get_cat_val );
              }

          }
          else if(sort_data && get_cat_val)
          {
             $.ajax({
              url:'/products',
              data:
              {
                'p_sort':sort_data,
                'p_cat':get_cat_val
              },
                 success: function (response) {
                 
                      
                     //$(".product_show_area").html($(response).find(".product_show_area"));
                      $(".product_show_area").html($(response).find(".product_show_area"));
                     
              
                 
              }
            });

              if (history.pushState) {
                  history.pushState(null, null, location.pathname + '?' + 'p_sort=' + sort_data + '&p_cat=' + get_cat_val );
              }

          }
          else if(get_cat_val)
          {
             $.ajax({
              url:'/products',
              data:
              {
                'p_cat':get_cat_val
              },
                 success: function (response) {
                 
                      
                     //$(".product_show_area").html($(response).find(".product_show_area"));
                      $(".product_show_area").html($(response).find(".product_show_area"));
                     
              
                 
              }
            });
              if (history.pushState) {
                  history.pushState(null, null, location.pathname + '?' +'p_cat=' + get_cat_val );
              }

          }    
         });
         $('input[name="filter_data"]').change(function(event)
         {
            console.log($(this).val());

            sort_data = $('#sort_by').val();
            get_cat_val= $('#product_category').val();
  
           
            var data={},filter_data=[];
            $('input[name="filter_data"]').each(function(i)
            {
                if (this.checked) {
                  if (!data.hasOwnProperty(this.name)) {
                      data[this.name] = [];
                  }
                  data[this.name].push(this.value);
                }

            });

             // get all keys.
            var keys = Object.keys(data);
            var filter_data = "";
             send_filter_data = "";
            // iterate over them and create the fdata
            keys.forEach(function(key,i){
              if (i>0) filter_data += '&';
              if (i>0) send_filter_data +='&'; // if its not the first key add &
              filter_data += key+"="+data[key].join(',');
              send_filter_data += data[key].join(',');
            });

            if(send_filter_data && sort_data && get_cat_val)
            {
                $.ajax({
                url:"/products",
                data:{
                  "filter_data":send_filter_data,
                  "p_sort":sort_data,
                  "p_cat":get_cat_val
                },
                 success: function (response) {
                  console.log(send_filter_data)
                      
                     //$(".product_show_area").html($(response).find(".product_show_area"));
                      $(".product_show_area").html($(response).find(".product_show_area"));
                     
              
                 
             }
            });
                 if (history.pushState) {
                  history.pushState(null, null, location.pathname + '?filter_data=' + send_filter_data + '&p_sort=' + sort_data + '&p_cat=' + get_cat_val );
              }

            } 
            else if(send_filter_data && sort_data)
            {
               $.ajax({
                url:"/products",
                data:{
                  "filter_data":send_filter_data,
                  "p_sort":sort_data
                  
                },
                 success: function (response) {
                  console.log(send_filter_data)
                      
                     //$(".product_show_area").html($(response).find(".product_show_area"));
                      $(".product_show_area").html($(response).find(".product_show_area"));
                     
              
                 
             }
            });
              if (history.pushState) {
                  history.pushState(null, null, location.pathname + '?filter_data=' + send_filter_data + '&p_sort=' + sort_data);
              }

            }
            else if(send_filter_data && get_cat_val)
            {
               $.ajax({
                url:"/products",
                data:{
                  "filter_data":send_filter_data,
                  "p_cat":get_cat_val
                  
                },
                 success: function (response) {
                  console.log(send_filter_data)
                      
                     //$(".product_show_area").html($(response).find(".product_show_area"));
                      $(".product_show_area").html($(response).find(".product_show_area"));
                     
              
                 
             }
            });

             if (history.pushState) {
                  history.pushState(null, null, location.pathname + '?filter_data=' + send_filter_data + '&p_cat=' + get_cat_val);
              }
            }
         
            else if(send_filter_data)
            {

            $.ajax({
                url:"/products",
                data:{
                  "filter_data":send_filter_data
                },
                 success: function (response) {
                  console.log(send_filter_data)
                      
                     //$(".product_show_area").html($(response).find(".product_show_area"));
                      $(".product_show_area").html($(response).find(".product_show_area"));
                     
              
                 
             }
            });

             if (history.pushState) {
                  history.pushState(null, null, location.pathname + '?filter_data=' + send_filter_data);
              }
            }
            else
            {
               $.ajax({
                url:"/show_all_products",
                 success: function (response) {

                      
                     //$(".product_show_area").html($(response).find(".product_show_area"));
                      $(".product_show_area").html($(response).find(".product_show_area"));
                     if (history.pushState) {
                  history.pushState(null, null, location.pathname);
              } 
              
                 
              }
            });
            }
          
        
            event.preventDefault();
         });

  });