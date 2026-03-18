function getFavouriteSongs(){
    const audioName = localStorage.getItem('FavAudioName');
    const audioFile = localStorage.getItem('FavAudioURL');

    if (not(audioName && audioFile) == null){
        document.addEventListener("DOMContentLoaded", function () {
            FavSounds = document.getElementsByID("FavouriteSoundsDiv");
            alert(FavSounds)
            // FavSounds.innerHTML += '<p>#1</p>'
            // FavSounds.innerHTML += "
            //     <button> 
            //         <img src="{% static 'images/MemeButton-removebg-preview.png' %}" alt="MemeButton" class="SoundButton" height="300em" width="300em"/>
            //     </button>"
               
        });
    }
}