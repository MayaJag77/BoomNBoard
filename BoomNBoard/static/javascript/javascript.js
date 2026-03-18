function changeImage(ButtonElement) {
    const clickedImage = ButtonElement.id;
    let ImageId = clickedImage.replace('LikeButton', "");
    ImageId = 'LikeImage' + ImageId;
    const img = document.getElementById(ImageId);
        if (img.src.includes("LikeButtonWhite.jpg")) {
            img.src = RedHeart;

        } else {
            img.src = WhiteHeart ;
        }
}

async function downloadSong(ButtonElement){
   // const clickedDownload = ButtonElement.getAttribute("data-name");
   // console.log(clickedDownload)
     
    const blob = new Blob([song1], { type: 'audio/mp3' });

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


