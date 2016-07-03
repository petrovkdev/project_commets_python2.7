function getXMLHttp()
{
  var xmlHttp

  try
  {
    //Firefox, Opera 8.0+, Safari
    xmlHttp = new XMLHttpRequest();
  }catch(e){
    //Internet Explorer
    try{
      xmlHttp = new ActiveXObject("Msxml2.XMLHTTP");
    }catch(e){
      try{
        xmlHttp = new ActiveXObject("Microsoft.XMLHTTP");
      }catch(e){
        alert("Your browser does not support AJAX!")
        return false;
      }
    }
  }
  return xmlHttp;
}

// submit form
function ajaxSubmit(){
  var req     = getXMLHttp(); 
  var val     = '';
  var require = document.getElementsByClassName('required');
  var cnt     = require.length;
  
  for (var i = 0; i < cnt; i++) {
    val = require[i].value;
    if(val == ''){
      require[i].className = 'control required invalide';
    }
    else{
      require[i].className = 'control required';
    }
  }
  
  var invalide = document.getElementsByClassName('required invalide');
  var cntInv = invalide.length;

  if(cntInv === 0){
    var firsName = document.getElementById("firstname").value,
        name     = document.getElementById("name").value,
        lastName = document.getElementById("lastname").value,
        region   = document.getElementById("region").value,
        city     = document.getElementById("city").value,
        code     = document.getElementById("code").value,
        phone    = document.getElementById("phone").value,
        email    = document.getElementById("email").value,
        comment  = document.getElementById("comment").value;
        
    document.getElementById("phone").className = 'control';
    document.getElementById("code").className = 'control';
    
    var reg = /^[\w-\.]+@[\w-]+\.[a-z]{2,4}$/i;
    var ml  = reg.test(email);
    
    if(code != '' && phone == ''){
      document.getElementById("phone").className = 'control invalide';
    }
    else if(code == '' && phone != ''){
      document.getElementById("code").className = 'control invalide';
    }
    else{
      if(!ml && email != ''){
        document.getElementById("email").className = 'control invalide';
      }
      else{
        document.getElementById("email").className = 'control';
        req.onreadystatechange = function(){
          if(req.readyState === 4){
            document.getElementById("send").className = 'none';
            document.getElementById("result").className = '';
            if(req.status === 200){
              var allfields = document.getElementsByClassName('control');
              var l = allfields.length;
              for(var f = 0; f < l; f++){
                allfields[f].value = '';
                document.getElementById('city').setAttribute('disabled','disabled');
              }
              document.getElementById("result").innerText = req.responseText;
              setTimeout(function(){
                document.getElementById("send").className = '';
                document.getElementById("result").className = 'none';
                document.getElementById("result").innerText = '';
              },3000);
            }
            else{
            
            }	
          }
        }   

        req.open('POST','/comment/',true);
        
        req.send('firstname='+firsName+'&name='+name+'&lastname='+lastName+'&region='+region+'&city='+city+'&code='+code+'&phone='+phone+'&email='+email+'&comment='+comment+'&ajax=Y&action=addcomment');
      }
     
    }
    
    
  }
  
}

// change select region
function changeRegion(s){
  
	var val = s.value;
	var req = getXMLHttp();
  
	req.onreadystatechange = function(){
		if(req.readyState === 4){
		
			if(req.status === 200){
				if(val == ''){
					document.getElementById('city').setAttribute('disabled','disabled');
				}else{
					document.getElementById('city').removeAttribute('disabled');
				}	
        document.getElementById('city').innerHTML = req.responseText;
			}
			else{
        
			}
			
		}
	
	}
  
	req.open('POST','/comment/',true);
  
	req.send("region="+val+"&ajax=Y&action=rchange");

}


// validate code, phone
document.getElementById("phone").onkeyup = keyupPhone;
document.getElementById("code").onkeyup = keyupPhone;

function keyupPhone(){
  var val    = this.value;
  var word   = val.replace(/\D/ig,'');
  this.value = word;
}

//validate email
document.getElementById("email").onblur = valideMail;
document.getElementById("email").onkeyup = keyupMail;

function valideMail(){
  var val    = this.value;
  var reg    = /^[\w-\.]+@[\w-]+\.[a-z]{2,4}$/i;
  var result = reg.test(val);
  
  if(!result && val != ''){
    this.className = 'control invalide';
  }
  else{
    this.className = 'control';
  }
}

function keyupMail(){
  this.className = 'control';
}



