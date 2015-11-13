var app = {
  config: {
      baseurl: ''
  }
};

app.Controller = {
  deletePerson: function(id){

    app.Model.delete(id).done(function(resp){

      if(resp.success){
        $('.modal').modal('hide');
        app.Controller.reload(app.config.baseurl);
      }
    });
  },

  addPerson: function(data){

    app.Model.add(data).done(function(resp){
        if(resp.success){
          app.Controller.reload(app.config.baseurl);
        }
    });
  },

  reload: function(path){
    window.location = path;
  }
};

app.Model = {
  delete: function(id){
    return $.post(app.config.baseurl + 'delete/' + id);
  },

  add: function(data){
    return $.post(app.config.baseurl + 'new', data)
  }
};