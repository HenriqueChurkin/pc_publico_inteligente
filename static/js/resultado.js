// Resultado (licitação): adicionar e remover linhas de propostas recebidas.
(function () {
  var area = document.getElementById('propostas');
  var botaoAdd = document.getElementById('add-proposta');
  if (!area || !botaoAdd) return;

  function novaLinha() {
    var n = area.querySelectorAll('.proposta-linha').length + 1;
    var div = document.createElement('div');
    div.className = 'proposta-linha';
    div.innerHTML =
      '<input type="text" name="proposta_nome" placeholder="Nome (ex.: Proposta ' + n + ')">' +
      '<input type="text" name="proposta_valor" inputmode="decimal" placeholder="Valor (R$)">' +
      '<button type="button" class="botao pequeno secundario remover-proposta">Remover</button>';
    area.appendChild(div);
    div.querySelector('input').focus();
  }

  botaoAdd.addEventListener('click', novaLinha);

  area.addEventListener('click', function (e) {
    if (e.target.classList.contains('remover-proposta')) {
      e.target.closest('.proposta-linha').remove();
    }
  });
})();
