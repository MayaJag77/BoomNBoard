function changeImage(ButtonElement) {
    const clickedImage = ButtonElement.id;
    let ImageId = clickedImage.replace('LikeButton', "");
    ImageId = 'LikeImage' + ImageId;
    const img = document.getElementById(ImageId);
        if (img.src.includes("LikeButtonWhite.jpg")) {
            img.src = RedHeart;
            addToFavourite(clickedImage)

        } else {
            img.src = WhiteHeart ;
        }
}

async function downloadSong(DownloadClicked) {
    const IDNumber = DownloadClicked.id.replace('DownloadButton', '');
    let audioID;

    if(IDNumber >=1 && IDNumber <=5){
         audioID = "audio" + IDNumber;
    } else if(IDNumber >=6 && IDNumber <=16){
         audioID = "audio_meme" + IDNumber
    } else if(IDNumber >=17 && IDNumber <=27){
         audioID = "audio_ringtone" + IDNumber
    } else if(IDNumber >=28 && IDNumber <=38){
         audioID = "audio_music" + IDNumber
    }

    const audioElement = document.getElementById(audioID);
    const src = audioElement.querySelector("source").getAttribute("src");

    const response = await fetch(src);
    const blob = await response.blob();

    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);

    const filename = src.split('/').pop();
    link.download = filename;

    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);

    URL.revokeObjectURL(link.href);
}


function addToFavourite(clickedImage){
    const IDNumber = clickedImage.replace('LikeButton', '')

    const audioID = "audio" + IDNumber
    const userID = window.UserID;

    
    audioName = document.getElementById(audioID)
    audioName = audioName.getAttribute("data-name");

    fetch("/home/save-fav/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({sound_id: IDNumber, user_id: userID ,})

    }).then(response => response.json()).then(data => {
        console.log("Server response: ", data)
    }).catch(error => console.error("Error: ", error));
    
}

function playSound(audioId) {
    const audio = document.getElementById(audioId);
    if (audio.paused) {
        audio.play();
    } else {
        audio.pause();
        audio.currentTime = 0;
    }
}

function toggleLike(button) {
    const img = button.querySelector('img');
    if (img.src.includes('LikeButtonWhite.jpg')) {
        img.src = img.src.replace('LikeButtonWhite.jpg', 'LikeButtonRed.jpg');
    } else {
        img.src = img.src.replace('LikeButtonRed.jpg', 'LikeButtonWhite.jpg');
    }
}