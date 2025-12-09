# Weather app

### Установка Docker на удаленный сервер
```sh
ansible-playbook -i hosts install_docker.yaml --ask-become-pass
```
### Развертывание веб приложения
```sh
ansible-playbook -i hosts deploy_app.yaml --ask-become-pass
```
### Развертывание мониторинга
```sh
ansible-playbook -i hosts deploy_monitoring.yaml --ask-become-pass
```
После выполения плейбуков, требуется добавить Dashboard, например с id 7587.