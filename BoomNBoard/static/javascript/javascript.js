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

async function downloadSong(ButtonElement){
   const clickedDownload = ButtonElement.getAttribute("data-name");
     
    const blob = new Blob([clickedDownload], { type: 'audio/mp3' });

        // Create a temporary link element
        const link = document.createElement('a');
        link.href = URL.createObjectURL(blob);
        link.download = clickedDownload +'.mp3'; // Suggested filename

        // Append link, trigger click, then remove
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);

        // Release the object URL
      try{
        URL.revokeObjectURL(link.href);
      } catch (error) {
        console.error("Download failed:", error);
      }
};

function addToFavourite(clickedImage){
    const IDNumber = clickedImage.replace('LikeButton', '')

    const audioID = "audio" + IDNumber

    audioList = []
    audioFileList = []
    audioName = document.getElementById(audioID)
    audioName = audioName.getAttribute("data-name");
    audioList.push(audioName)
    audioFile = document.getElementById(audioID)
    audioFile = audioFile.src
    audioFileList.push(audioFile)

    localStorage.setItem('FavAudioName', audioList);
    localStorage.setItem('FavAudioURL', audioFileList)
    
}


