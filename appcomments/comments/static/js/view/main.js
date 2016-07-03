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

function delComment(el){
  var id = el.getAttribute('data-id');
  var comment = document.getElementById(id);
  comment.parentNode.removeChild(comment);
  
  var req = getXMLHttp();
  var index = parseInt(id.replace(/comment-/,''));
  
  var size = document.getElementsByClassName('row').length;

	req.onreadystatechange = function(){
		if(req.readyState === 4){
		
			if(req.status === 200){
        document.getElementById('result').className = '';
        setTimeout(function(){
          document.getElementById('result').className = 'none';
        },3000);
        
        if(size == 0){
          document.getElementById('content').innerHTML = '<h3>Нет комментариев для просмотра!<h3>';
        }
			}
			else{
        
			}
			
		}
	
	}
  
	req.open('POST','/view/',true);
  
	req.send("id="+index+"&ajax=Y&action=delcomment");
}

