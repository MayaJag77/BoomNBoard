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
    const audioID = "audio" + IDNumber;

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
    
    audioName = document.getElementById(audioID)
    audioName = audioName.getAttribute("data-name");
    audioUser = document.getElementById(audioID)
    audioUser = audioUser.getAttribute("data-user")
    // alert(audioUser)
    // audioFile = document.getElementById(audioID)
    // audioFile = audioFile.src

    fetch("/home/save-fav/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({appuser:audioUser, sound:audioName.soundFile})
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