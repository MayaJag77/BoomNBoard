function changeImage(ButtonElement) {
    const clickedImage = ButtonElement.id
    let ImageId = clickedImage.replace('LikeButton', "");
    ImageId = 'LikeImage' + ImageId
    const img = document.getElementById(ImageId)
        if (img.src.includes("LikeButtonWhite.jpg")) {
            img.src = RedHeart
        } else {
            img.src = WhiteHeart 
        }
}

function downloadSong(ButtonElement){
    const clickedDownload = ButtonElement.id
    alert(clickedDownload + "Has been clicked!")
}