var app = {};

app.Controller = {
  deletePerson: function(id){
    app.Model.delete(id).done(function(resp){
      $('.modal').modal('hide');
    });
  }
};


app.Model = {
  delete: function(id){
    return $.post('/delete/' + id);
  }
};