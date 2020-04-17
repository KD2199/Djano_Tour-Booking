function check()
  {
    var name=document.getElementById('email');
    var pwd=document.getElementById('password');
   
    if(name.value.trim()=="")
    {
      //alert("Username is blank...");
      document.getElementById("7").style.visibility="visible";
      return false;
    }
    else if(pwd.value.length<8)
    {

      //alert("Password is blank...");
      document.getElementById("8").style.visibility="visible";
      return false;
    }

    else
    {
      true;
  }