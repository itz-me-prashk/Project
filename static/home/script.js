{var add1=document.getElementById("pop")

var add2=document.getElementById("form")

var addbtn=document.getElementById("new")

var cnbtn=document.getElementById("cancel")

var save1=document.getElementById("save")

var xmark1=document.querySelector("x-mark")

var ediths=document.querySelector('.edith')
function list()
{
	add1.style.display="block"
	add2.style.display="block"
}

addbtn.addEventListener("click",function(){
	add1.style.display="block"
	add2.style.display="block"
})
// ediths.addEventListener("click",function(){
// 	add1.style.display="block"
// 	add2.style.display="block"
// })

cnbtn.addEventListener("click",function(){
	add1.style.display="none"
	add2.style.display="none"
})


}

	// var author=document.querySelector(".bname")
	
	var title=document.querySelector(".btitle")
	
	var descript=document.querySelector(".cont")
	
	var content =document.querySelector("#container")
	
	var save=document.querySelector(".save")
	
	
	
	// save.addEventListener("click",function(){
	// 	var div = document.createElement("div")
	// 	div.setAttribute("class","text1")
		
	// 	div.innerHTML=`<h2>${title.value}</h2>
		               
	// 	               <p>${descript.value}</p>
	// 	               <button onclick="delall(event)" class="callit" >Delete</button>
	// 	               `
	// 	content.append(div)

	// 	ce()
	// 	add1.style.display="none"
	//     add2.style.display="none"
		
	// })
	
	// function delall(event)
	// {
	// 	event.target.parentElement.remove()
	// }
	function ce()
	{
		// document.querySelector(".bname").value=""
		title.value=""
		descript.value=""
	}
	function cancel1()
	{
		add1.style.display="none"
	    add2.style.display="none"
	}
	var sub=document.querySelector('.save')
	