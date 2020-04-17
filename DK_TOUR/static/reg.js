function check()
    {
      var email=document.getElementById('email');
      var pwd=document.getElementById('password');
      var rpass=document.getElementById('rpassword');
      var uname=document.getElementById('uname');

      if(uname.value.trim()=="" )
      {
        //alert("Username is blank...");
        document.getElementById("12").style.visibility="visible";
        return false;
      }

     
      else if(email.value.trim()=="" )
      {
        //alert("Username is blank...");
        document.getElementById("7").style.visibility="visible";
        return false;
      }
      
      else if(pwd.value.length<8)
      {
        /*alert("Password is too short...");*/
        document.getElementById("8").style.visibility="visible";
        return false;
      }
      else if(pwd.value!=rpass.value)
      {
        //alert("Password is blank...");
        document.getElementById("9").style.visibility="visible";
        return false;
      }
      {
        true;
      }
    }