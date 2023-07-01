 // Function to show and hide the popup
 function togglePopup(elId) {
	 
	 for (var i=1; i <= 3; i++) {
			//alert('l'+i);	
				//$('.close-btn'+i).toggle();
			}
				//document.getElementById('l'+elId).className = 'show';
            //$(".SecInEntry").toggle();
			$('.SecInEntry'+elId).toggle();
        }


		
// Button Onclick Active

function show(elId) {
		for (var i=1; i <= 2; i++) {
			//alert('i'+i);	
			//var bro=document.getElementById('sidebarbtnBlock').tagName.getElementById;
				document.getElementById('l'+i).className = 'hide';
				document.getElementById('bnt00'+i).className = 'INactive';
				
			}
				document.getElementById('l'+elId).className = 'show';
				document.getElementById('bnt00'+elId).className = 'active';
				//document.getElementById('sidebarbtnBlock').tagName.className = 'active';
		}
		
		//document.getElementByClassName('sidebarbtn').className = 'active';
//End of Button Onclick Active



function toggleMobileMenu(menu){
	menu.classList.toggle('open');
}