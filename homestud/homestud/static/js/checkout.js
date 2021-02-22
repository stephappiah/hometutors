
$(document).ready(function(){
    // insert loading div into top of document
    $('body').prepend("<div class='loading hidden'><div class='uil-ring-css' style='transform:scale(0.79);'><div></div>");

    function payWithPaystack() {

        let handler = PaystackPop.setup({
            key: publicKey, // Replace with your public key
            email: user_email,
            amount: amount_to_pay * 100,
            currency: 'GHS', // Use GHS for Ghana Cedis or USD for US Dollars
            ref: ''+Math.floor((Math.random() * 1000000000) + 1), // generates a pseudo-unique reference. Please replace with a reference you generated. Or remove the line entirely so our API will generate one for you
            // label: "Optional string that replaces customer email"

            onClose: function(){
                 // show alert
                 $('.alert').removeClass('hide').addClass('alert-danger show');
                 // set text
                 $('.alert-message').text('Transaction failed!');
                 //   redirect to next or home
            },

            // after paystack transaction
            callback: function(response){

                // verify transaction on /payment/verify-transaction
                
                $.ajax({
                    url: '/pay/verify-payment/'+ response.reference,
                    method: 'get',
                    beforeSend: function(){
                        // show loading screen
                        var loadingOverlay = document.querySelector('.loading');

                        document.body.blur();
                        loadingOverlay.classList.remove('hidden');
                
                    },
                    success: function (response) {
                        // hide loading screen
                        var loadingOverlay = document.querySelector('.loading');

                        document.body.blur();
                        loadingOverlay.classList.add('hidden');

                      // the transaction status is in response.data.status
                      if(response[3].status == 'success'){
                        
                           // show alert
                        $('.alert').removeClass('hide').addClass('alert-success show');
                        // set text
                        $('.alert-message').text('Transaction successful!');
                        // redirect to next page --> chat

                      } else {

                          // show alert
                        $('.alert').removeClass('hide').addClass('alert-danger show');
                        // set text
                        $('.alert-message').text('Transaction failed!');
                        //   redirect to next or home
                      }
                      
                      console.log(response);
                    }
                  });
            }
        });

        handler.openIframe();
    }

    // on click run payment function
    // var payBtn = document.getElementById('pay-btn');
    // payBtn.addEventListener('click', payWithPaystack);
    $('#pay-btn').on('click', payWithPaystack);
})