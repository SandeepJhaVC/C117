//Create date variable
var date = new Date()
let display_date = "Date:"+date.toLocaleDateString()

//Load HTML DOM
$(document).ready(function(){
    $("#display_date").html(display_date)
})


//Define variable to store predicted emotion
let predicted_emotion

$(function () {
    $("#predict_button").click(function () {
        let input_data = {
            "text":$("#text").val()
        }
        console.log(input_data)
        //AJAX call

        $.ajax({
            type:'POST',
            url:'/predict-emotion',
            data:JSON.stringify(input_data),
            datatypes:"json",
            contentType:'application/json',
            success:function(result){
                $('#prediction').html(result.data.predicted_emotion)
                $('#emo_img_url').attr('src', result.data.predicted_emotion_img_url);
                $("#prediction").css('display','');
                $("#emo_img_url").css("diaplay",'')
                predicted_emotion=result.data.predicted_emotion
                $('#save_button').prop('disabled', false)
            },

            error : function(result){
                alert(result.responseJSON.message)
            }
            
              
        });
    });

    $('#save_button').click(function(){
        save_data={
            "date":display_date,
            "text":$("#text").val(),
            "emotion": predicted_emotion
        }
        $.ajax({
            type:"POST",
            url:"/save-entry",
            data:JSON.stringify(save_data),
            dataType:"json",
            contentType:'application/json',
            success:function(result){
                alert("Your entry has been saved successfuly")
                window.location.reload()
            },
            error:function(result){
                alert(result.responseJSON.message)
            }
        })
    })
})

