window.onload = function() {
    var progressBar = document.getElementById('progressBar');
    var width = 0;
    var id=0
    var interval = setInterval(function() {
        if (width >= 100 && id==0) {
            clearInterval(interval);

            window.location.href = '/signin'; 
            id=1
        } 
        // if else (width >= 20){
        //     text.textContent='Configuring DataBase'
        // }
        // if else(width>=50){
        //     text.textContent='Getting UserDetails'
        // }
        else {
            width++;
            progressBar.style.width = width + '%';
            if (width>=50){
                var text=document.querySelector('.tit')
                text.textContent='Please Wait - Configuring DataBase'
            }
            if (width>=70){
                var text=document.querySelector('.tit')
                text.textContent='Please Wait - Getting UserDetails'
            }
            if (width>=90){
                var text=document.querySelector('.tit')
                text.textContent='Please Wait - Almost Done'
            }
        }
    }, 55);
};
