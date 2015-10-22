require(["gitbook"], function(gitbook) {
    // Bind a quiz
    var prepareQuiz = function($quiz) {

        $quiz.find(".quiz-answers input").click(function(e) {
            //e.preventDefault();
        });

        // Submit: test code
        $quiz.find(".action-submit").click(function(e) {
            //console.log("dsdfsfsdfdsfsfd");
            //e.preventDefault();
            gitbook.events.trigger("exercise.submit", {type: "quiz"});
            $quiz.find("tr.alert-danger,li.alert-danger").removeClass("alert-danger");
            $quiz.find(".alert-success,.alert-danger").addClass("hidden");

            var answer='';
            var tk='';
            $quiz.find(".question").each(function(q) {
                var result = true;

                var $questions = $(this).find(".question-content").find("input[type=radio], input[type=checkbox]");
                var $answers = $(this).find(".question-answers").find("input[type=radio], input[type=checkbox]");
                 
                var $text =$(this).find(".question-content").find("input[type=text]");

                //console.log($text);
                if($text)
                {
                  $text.each(function(){
                     tk+=$(this).val()+'|';
                  });
                }
                 //console.log("tk"+tk);
                //console.log($questions)
                //console.log($answers)
                $questions.each(function(i) {
                    //console.log($(this));
                    
                    //console.log(fname);
                    if($(this).is(":checked"))
                    {
                      console.log(i);
                      if(i==0)
                       answer +='A';
                      if(i==1)
                       answer +='B';
                      if(i==2)
                       answer +='C';
                      if(i==3)
                       answer +='D';
                      if(i==4)
                       answer +='E';
                      if(i==5)
                       answer +='F';
                      if(i==6)
                       answer +='G';
                      if(i==7)
                       answer +='H';
                      if(i==8)
                       answer +='I';
                      if(i==9)
                       answer +='J';
                    }
                    var correct = $(this).is(":checked") === $answers.slice(i).first().is(":checked");
                    result = result && correct;
                    if (!correct) {
                        $(this).closest("tr, li").addClass("alert-danger");
                    }
                });
                var url = window.location.pathname;
                var fname = url.substring(0, url.lastIndexOf('.'));

                console.log(window.location.search);
                name = getquerystring("username");
                email = getquerystring("email");
                //console.log(name);
               // console.log(name.length);
                //console.log(email);
                //console.log(email.length);
                if(name!="null" && email.length!=0)
                    {

                        if(tk!="")
                         {
                           newtk=tk.substring(0, tk.length-1)
                           console.log(newtk)
                           var mydata={ "url":url,
                                     "protocol":window.location.protocol,
                                     "allurl":window.location.host,
                                     "username":name,
                                     "email":email,
                                     "answer":newtk
                                   };
		          var ws = new WebSocket('ws://192.168.0.253:3368');
		          ws.onopen = function(){
                            console.log("send");
		            ws.send(JSON.stringify(mydata));
                           };
		          ws.onmessage = function(result){console.log(result.data);}
		          ws.onclose=function(evt){console.log("close");};
		          ws.onerror=function(evt){console.log("error");};
                           
                         }
                        if(tk=="" && answer!="")
                       {
                        var mydata={ "url":url,
                                     "protocol":window.location.protocol,
                                     "allurl":window.location.host,
                                     "username":name,
                                     "email":email,
                                     "answer":answer
                                   };
		        var ws = new WebSocket('ws://192.168.0.253:3368');
		        ws.onopen = function(){
                          console.log("send");
		          ws.send(JSON.stringify(mydata));
                        };
		        ws.onmessage = function(result){console.log(result.data);}
		        ws.onclose=function(evt){console.log("close");};
		        ws.onerror=function(evt){console.log("error");};
                      }
                   }
              //  $(this).find(result ? "div.alert-success" : "div.alert-danger").toggleClass("hidden");
            });

        });

        $quiz.find(".action-solution").click(function(e) {
            e.preventDefault();
            $quiz.find(".question-content, .question-answers").toggleClass("hidden");
        });
    };

   function getquerystring(argv_name){

     var reg = new RegExp("(^|&)" + argv_name + "=([^&]*)(&|$)","i");
     var r = window.location.search.substr(1).match(reg);
     if (r!=null) return unescape(r[2]);
     return null;

   };
    
    // Prepare all exercise
    var init = function() {
        gitbook.state.$book.find("section.quiz").each(function() {
            prepareQuiz($(this));
        });
    };

    gitbook.events.bind("page.change", function() {
       // alert("dadasdasdas");
        
        init();
    });
});
