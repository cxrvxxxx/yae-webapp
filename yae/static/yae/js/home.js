function copyLink() {
    var copyText = document.getElementById("inviteLinkField");
    copyText.select();
    copyText.setSelectionRange(0, 99999);
    navigator.clipboard.writeText(copyText.value);
    const btn = document.getElementById("copyLinkBtn");
    btn.addEventListener("click", ()=>{
        btn.value = "LINK COPIED!";
    });
  }
