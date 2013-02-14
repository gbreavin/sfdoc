def __get_class_item(classname):
	return '<li><a href="' + classname + '.html">' + classname + '</a></li>'

def __get_author_content(author):
	return '<li>' + author.name + '</li>'

def __get_param_content(param):
	return '<tr><td>' + param.name + '</td><td>' + param.param_type + '</td><td>' + param.description + '</td></tr>'

def __fill_in_method_content(content_method, minfo):
	new_content = content_method.replace('[methodname]', minfo.name)
	param_content = [__get_param_content(p) for p in minfo.params]
	new_content = new_content.replace('[params]', ''.join(param_content))
	new_content = new_content.replace('[returntype]',minfo.return_type)
	new_content = new_content.replace('[returndescription]',minfo.return_description)
	return new_content

def __fill_in_class_content(content_master, content_method, cinfo, project_name):
	new_content = content_master.replace('[projectname]', project_name)
	new_content = new_content.replace('[classname]', cinfo.name)
	new_content = new_content.replace('[since]', cinfo.since)
	author_content = [__get_author_content(a) for a in cinfo.authors]
	new_content = new_content.replace('[authors]', ''.join(author_content))
	method_content = [__fill_in_method_content(content_method, minfo) for minfo in cinfo.methods]
	new_content = new_content.replace('[methodlist]', ''.join(method_content))
	return new_content

def create_outfile(classlist, cinfo, target, template_master='template_master.html', template_method='template_method.html', project_name='Apex Documentation'):
	content_master = ''
	with open(template_master) as f:
		content_master = f.read()
	content_method = ''
	with open(template_method) as f:
		content_method = f.read()
	
	new_content = __fill_in_class_content(content_master, content_method, cinfo, project_name)
	class_items = [__get_class_item(c) for c in classlist]
	new_content = new_content.replace('[classlist]', ''.join(class_items))
	with open(target, 'w+') as f:
		f.write(new_content)