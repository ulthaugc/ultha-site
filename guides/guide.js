(function(){
  // reading progress bar
  var bar=document.querySelector('.progress');
  if(bar){var f=function(){var h=document.documentElement,max=h.scrollHeight-h.clientHeight;bar.style.width=(max>0?(h.scrollTop/max*100):0)+'%'};addEventListener('scroll',f,{passive:true});f()}
  // copy buttons: copies the nearest .qt (question) or [data-copy] target
  document.querySelectorAll('.copy').forEach(function(b){
    b.addEventListener('click',function(){
      var src=b.dataset.target?document.getElementById(b.dataset.target):b.parentNode.querySelector('.qt');
      var t=(src?src.innerText:'').replace(/^"|"$/g,'').trim();
      var done=function(){var o=b.textContent;b.textContent='Copied ✓';setTimeout(function(){b.textContent=o},1600)};
      if(navigator.clipboard){navigator.clipboard.writeText(t).then(done,done)}else{done()}
    });
  });
  // reveal sample answers
  document.querySelectorAll('.reveal').forEach(function(b){b.addEventListener('click',function(){b.parentNode.classList.add('open')})});
  // tabs
  document.querySelectorAll('[role=tablist]').forEach(function(list){
    var tabs=list.querySelectorAll('[role=tab]');
    tabs.forEach(function(t){t.addEventListener('click',function(){
      tabs.forEach(function(x){x.setAttribute('aria-selected','false');document.getElementById(x.getAttribute('aria-controls')).classList.remove('on')});
      t.setAttribute('aria-selected','true');document.getElementById(t.getAttribute('aria-controls')).classList.add('on');
    })});
  });
})();
// highlight the current section in the "On this page" list
(function(){var links=[].slice.call(document.querySelectorAll('.toc2 a'));if(!links.length||!('IntersectionObserver' in window))return;
var map={};links.forEach(function(a){map[a.getAttribute('href').slice(1)]=a});
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){links.forEach(function(l){l.classList.remove('on')});var a=map[e.target.id];if(a)a.classList.add('on')}})},{rootMargin:'0px 0px -70% 0px'});
Object.keys(map).forEach(function(id){var h=document.getElementById(id);if(h)io.observe(h)})})();
// show digits in the body font wherever the headline serif is used (its numerals are old-style)
(function(){
  var w=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT,null),n,todo=[];
  while((n=w.nextNode())){ if(/\d/.test(n.nodeValue)&&n.parentNode&&!n.parentNode.closest('script,style,svg,.nf')&&/Young Serif/i.test(getComputedStyle(n.parentNode).fontFamily)) todo.push(n); }
  todo.forEach(function(t){var f=document.createDocumentFragment();t.nodeValue.split(/(\d[\d.,%$→:]*)/).forEach(function(p,i){if(!p)return;if(i%2){var s=document.createElement('span');s.className='nf';s.textContent=p;f.appendChild(s)}else f.appendChild(document.createTextNode(p))});t.parentNode.replaceChild(f,t)});
})();
