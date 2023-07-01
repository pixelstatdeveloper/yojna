$(() => {
  const application_form = $('#application_form')
  const document_form = $('#kagadpatre')
  const scanned_form = $('#scanned_form')

  console.log(application_form, document_form)

  document_form.on('submit', (event) => {

    if(scanned_form[0].value !== '') {
      return document_form[0].reportValidity()
    }
    event.preventDefault()
    const form = application_form
    const url = form.attr('action');
    
    if(!application_form[0].reportValidity()) {
      alert('Please fill out all the fields')
      return
    }

    $.ajax( {
      url,
      type: 'POST',
      data: new FormData(form[0]),
      processData: false,
      contentType: false,
      success: function (data) {
        console.log(data)
        try{
          if(data?.status && data.status === 200) {
            document.getElementById('application_form_wrapper').remove()
            document_form[0].submit()
          }else{
            alert(data.error)
          }
        }
        catch{
          alert(data.error)
        }
      },
      fail: function () {
        console.log('Request to API Failed')
        alert('Server Error: Please retry later')
      }
    });
  })
})
