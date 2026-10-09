(() => {
const input=document.getElementById('mri_image'), drop=document.getElementById('dropzone'), preview=document.getElementById('preview');
const title=document.getElementById('dropTitle'), subtitle=document.getElementById('dropSubtitle'), line=document.getElementById('fileline');
const name=document.getElementById('filename'), clear=document.getElementById('clearFile'), form=document.getElementById('uploadForm'), submit=document.getElementById('submitButton');
function show(f){if(!f)return;if(!['image/jpeg','image/png'].includes(f.type)){alert('Choose a JPG, JPEG, or PNG image.');input.value='';return}
if(f.size>5*1024*1024){alert('Maximum image size is 5 MB.');input.value='';return}
name.textContent=f.name+' · '+(f.size/1024<1024?Math.round(f.size/1024)+' KB':(f.size/1048576).toFixed(2)+' MB');line.hidden=false;title.textContent='Image ready to analyze';subtitle.textContent='Check the preview, then start analysis';preview.replaceChildren();const img=document.createElement('img');img.alt='Selected MRI preview';img.src=URL.createObjectURL(f);preview.append(img)}
input.addEventListener('change',()=>show(input.files[0]));
['dragenter','dragover'].forEach(t=>drop.addEventListener(t,e=>{e.preventDefault();drop.classList.add('dragging')}));
['dragleave','drop'].forEach(t=>drop.addEventListener(t,e=>{e.preventDefault();drop.classList.remove('dragging')}));
drop.addEventListener('drop',e=>{const f=e.dataTransfer.files[0];if(!f)return;const dt=new DataTransfer();dt.items.add(f);input.files=dt.files;show(f)});
clear.addEventListener('click',()=>{input.value='';line.hidden=true;title.textContent='Drop your MRI image here';subtitle.textContent='or click to browse files';preview.textContent='⇧'});
form.addEventListener('submit',e=>{if(!input.files.length){e.preventDefault();alert('Please select an MRI image first.');return}submit.disabled=true;submit.textContent='Processing image…'});
document.getElementById('menuToggle').addEventListener('click',()=>document.getElementById('sidebar').classList.toggle('open'));
document.querySelectorAll('.sidebar nav a').forEach(a=>a.addEventListener('click',()=>document.getElementById('sidebar').classList.remove('open')));
})();
