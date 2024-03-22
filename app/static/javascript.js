
// Função para incluir novo item
function enviarFormulario() {
  var formulario = document.getElementById((id = "carroForm"));
  //funcao para conferir formulario
  // se erro abortar envio

  var formData = new FormData(formulario);
  var objeto = {};
  formData.forEach(function (value, key) {
    objeto[key] = value
    // validateForm(value) //valida se o campo esta vazio ou null
  });
  var json = JSON.stringify(objeto);
  // Agora você pode enviar o JSON usando fetch() ou outra biblioteca de sua escolha
  fetch("/veiculo", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: json,
  })
    .then(response => {
      if (response.ok) {
        alert('Veículo adicionado com sucesso');
        location.reload(); // Atualiza a página
      } else {
        throw new Error('Ocorreu um erro ao incluir o veículo');
      }
    })
    .catch(error => {
      alert(error.message);
    });
}

// Adiciona evento de clique nos botões de exclusão
document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll('.excluir-carro-btn').forEach(item => {
    item.addEventListener('click', function (event) {
      const id_veiculo = this.getAttribute('data-id');
      // showConfirmDeleteModal(id_veiculo);
      const botao = document.querySelector('.delete-carro-btn');
      botao.setAttribute('data-id', id_veiculo);

    });
  });
});

// Adiciona evento de clique no botão de delete do veiculo (modal)
document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll('.delete-carro-btn').forEach(item => {
    item.addEventListener('click', function (event) {
      const id_veiculo = this.getAttribute('data-id');
      deleteCarro(id_veiculo);
    });
  });
});

// Função para enviar a solicitação de exclusão
function deleteCarro(id) {
  fetch(`/veiculo/${id}`, {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json'
    }
  })
    .then(response => {
      if (response.ok) {
        alert('Veículo removido com sucesso');
        location.reload(); // Atualiza a página
      } else {
        throw new Error('Ocorreu um erro ao excluir o veículo');
      }
    })
    .catch(error => {
      alert(error.message);
    });
}

// Adiciona evento de atualizar value dos inputs
document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll('.edit-carro-btn').forEach(item => {
    item.addEventListener('click', function (event) {
      const id_veiculo = this.getAttribute('data-id');
      const botao = document.querySelector('.atualizar-carro-btn');
      botao.setAttribute('data-id', id_veiculo);
      getCar(id_veiculo)
    });
  });
});

function getCar(id_veiculo) {

  fetch(`/veiculo/${id_veiculo}`, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json'
    }
  })
    .then(response => {
      if (response.ok) {
        return response.json(); // Retorna os dados do carro como JSON
      } else {
        throw new Error('Falha ao obter os dados do carro');
      }
    })
    .then(data => {
      console.log(data.content);
      const carroData = data.content; // Considerando que o objeto retornado já contém os dados do carro
      // Percorre o JSON e define o valor de cada campo de entrada correspondente
      Object.keys(carroData).forEach(key => {
        let value = carroData[key];
        let id_name = `${key}-carro-edit`;
        const inputField = document.getElementById(id_name);
        if (inputField) {
          inputField.value = value;
        }
      });
    })
    .catch(error => {
      alert(error.message);
    });
}


// Adiciona evento de clique nos botões de atualizar o veiculo
document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll('.atualizar-carro-btn').forEach(item => {
    item.addEventListener('click', function (event) {
      const id_veiculo = this.getAttribute('data-id');
      updateCarro(id_veiculo)
    });
  });
});

// Função para editar item
function updateCarro(id_veiculo) {
  var formulario = document.getElementById((id = "carroFormEdit"));
  var formData = new FormData(formulario);
  var objeto = {};

  formData.forEach(function (value, key) {
    objeto[key] = value;
    // validateForm(value)
  });
   //valida se o campo esta vazio ou null
  var json = JSON.stringify(objeto);

  // Agora você pode enviar o JSON usando fetch() ou outra biblioteca de sua escolha
  fetch(`/veiculo/${id_veiculo}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json'
    },
    body: json,
  })
    .then(response => {
      if (response.ok) {
        alert('Veículo editado com sucesso');
        location.reload(); // Atualiza a página
      } else {
        throw new Error('Ocorreu um erro ao editar o veículo');
      }
    })
    .catch(error => {
      alert(error.message);
    });
}

// modal Bulma 
document.addEventListener('DOMContentLoaded', () => {
  // Functions to open and close a modal
  function openModal($el) {
    $el.classList.add('is-active');
  }

  function closeModal($el) {
    $el.classList.remove('is-active');
  }

  function closeAllModals() {
    (document.querySelectorAll('.modal') || []).forEach(($modal) => {
      closeModal($modal);
    });
  }

  // Add a click event on buttons to open a specific modal
  (document.querySelectorAll('.js-modal-trigger') || []).forEach(($trigger) => {
    const modal = $trigger.dataset.target;
    const $target = document.getElementById(modal);

    $trigger.addEventListener('click', () => {
      openModal($target);
    });
  });

  // Add a click event on various child elements to close the parent modal
  (document.querySelectorAll('.modal-background, .modal-close, .modal-card-head .delete, .modal-card-foot .button') || []).forEach(($close) => {
    const $target = $close.closest('.modal');

    $close.addEventListener('click', () => {
      closeModal($target);
    });
  });

  // Add a keyboard event to close all modals
  document.addEventListener('keydown', (event) => {
    if (event.key === "Escape") {
      closeAllModals();
    }
  });
});

// Função que validade os campos dos formulários de adicionar e editar o carro
function validateForm(value) {

    if (value == (null || "")) {
      alert('"Por favor, preencha todos os campos!"');
      return false;
  };

}