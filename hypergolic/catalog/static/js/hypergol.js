$(function(){
    $('form').addClass('col-sm-4');
    $('form').find('select, [type=text], [type=password], [type=email],\
                    [type=url], [type=search], [type=datetime-local], textarea,\
                    [type=date], [type=month], [type=time], [type=week],\
                    [type=number], [type=tel], [type=color]').addClass('form-control');
    $('form').children('div, p').addClass('form-group');
    $('form').find('[type=file]').addClass('form-control-file');
    $('form').find('[type=radio], [type=checkbox]').addClass('form-check-input');
    $('form').find('[type=radio], [type=checkbox]').parent('div, p').addClass('form-check');
    $('form').find('[type=radio], [type=checkbox]').sibling('label').addClass('form-check-label');
    $('form').find('[type=submit]').addClass('btn btn-primary');
});