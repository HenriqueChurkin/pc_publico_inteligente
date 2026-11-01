// Etapa 1: ao escolher a finalidade, troca a lista de softwares (com os padrões já marcados).
(function () {
  var dados = JSON.parse(document.getElementById('dados-finalidades').textContent);
  var lista = document.getElementById('lista-softwares');

  function mostrar(finalidadeId) {
    var f = dados[finalidadeId];
    lista.innerHTML = '';
    if (!f) return;

    if (finalidadeId === 'outra') {
      lista.innerHTML = '<p class="nota">Nesta finalidade você informa os requisitos manualmente na próxima etapa.</p>';
      return;
    }
    f.opcoes.forEach(function (s) {
      var marcado = f.padrao.indexOf(s.id) !== -1;
      var rotulo = document.createElement('label');
      rotulo.className = 'opcao' + (marcado ? ' marcada' : '');
      rotulo.innerHTML =
        '<input type="checkbox" name="softwares" value="' + s.id + '"' + (marcado ? ' checked' : '') + '>' +
        '<span></span><small>fonte: ' + s.fonte + '</small>';
      rotulo.querySelector('span').textContent = s.nome;   // textContent evita problemas com caracteres especiais
      lista.appendChild(rotulo);
    });
  }

  document.querySelectorAll('input[name="finalidade"]').forEach(function (r) {
    r.addEventListener('change', function () { mostrar(r.value); });
  });
})();
