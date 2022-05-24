
  function disappear() {
    document.getElementById("sub").style.display = "none"
  }
 
  function increase() {
    document.getElementById("ninjaScore").innerHTML=a;
                a=a+1;
  }

  function incrementNinjas(diff) {
    var count = document.getElementById('ninjaScore');
    ninjaScore.innerText = +ninjaScore.innerText + diff;
  }

  function incrementPirates(diff) {
    var count = document.getElementById('pirateScore');
    pirateScore.innerText = +pirateScore.innerText + diff;
  }