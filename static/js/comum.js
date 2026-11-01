// Funções usadas em várias telas.

// 1) Botões "Copiar": <button data-copiar="#id-do-elemento">
document.querySelectorAll('[data-copiar]').forEach(function (botao) {
  botao.addEventListener('click', function () {
    var alvo = document.querySelector(botao.dataset.copiar);
    if (!alvo) return;
    var texto = ('value' in alvo && alvo.tagName !== 'LI') ? alvo.value : alvo.innerText;
    var textoOriginal = botao.textContent;

    function feito() {
      botao.textContent = 'Copiado!';
      setTimeout(function () { botao.textContent = textoOriginal; }, 1500);
    }
    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText(texto).then(feito);
    } else {   // plano B para http sem https
      var tmp = document.createElement('textarea');
      tmp.value = texto;
      document.body.appendChild(tmp);
      tmp.select();
      document.execCommand('copy');
      document.body.removeChild(tmp);
      feito();
    }
  });
});

// 2) Aviso de marca, modelo ou geração enquanto o texto é digitado:
//    <textarea data-verificar-termos="#id-da-caixa-de-aviso">
document.querySelectorAll('[data-verificar-termos]').forEach(function (area) {
  var caixa = document.querySelector(area.dataset.verificarTermos);
  var espera = null;

  function verificar() {
    fetch('/conferir/termos', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ texto: area.value })
    })
      .then(function (r) { return r.json(); })
      .then(function (termos) {
        if (!termos.length) { caixa.hidden = true; return; }
        var lista = termos.map(function (t) { return '“' + t.termo + '” (' + t.tipo + ')'; }).join(', ');
        caixa.textContent = 'Atenção: o texto cita marca, linha de produto ou geração: ' + lista +
          '. Em licitação, descreva por desempenho e aceite "equivalente ou superior".';
        caixa.hidden = false;
      });
  }

  area.addEventListener('input', function () {
    clearTimeout(espera);
    espera = setTimeout(verificar, 400);
  });
  if (area.value.trim()) verificar();
});

// 3) Destaque visual das opções marcadas (radio e checkbox dentro de .opcao)
document.addEventListener('change', function (e) {
  var campo = e.target;
  if (!campo.closest || !campo.closest('.opcao')) return;
  if (campo.type === 'radio') {
    document.querySelectorAll('input[type=radio][name="' + campo.name + '"]').forEach(function (r) {
      r.closest('.opcao').classList.toggle('marcada', r.checked);
    });
  } else {
    campo.closest('.opcao').classList.toggle('marcada', campo.checked);
  }
});
