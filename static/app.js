var app = {};

app.Controller = {
  deletePerson: function(id){

    app.Model.delete(id).done(function(resp){

      if(resp.success){
        $('.modal').modal('hide');
        app.Controller.reload("/");
      }
    });
  },

  addPerson: function(data){

    app.Model.add(data).done(function(resp){
        if(resp.success){
          app.Controller.reload("/");
        }
    });
  },

  reload: function(path){
    window.location = path;
  }
};

app.Model = {
  delete: function(id){
    return $.post('delete/' + id);
  },

  add: function(data){
    return $.post('new', data)
  }
};