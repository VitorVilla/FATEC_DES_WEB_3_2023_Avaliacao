from django.test import TestCase
from .models import faculdade
from .forms import TaskForm

class getTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/listar/')
        
    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)
        
    def test_page_title(self):
        self.assertContains(self.resp, 'Todas os alunos')
        
    def test_template_home(self):
        self.assertTemplateUsed('list.html')
        
class postTest(TestCase):
    def setUp(self):
        self.getResp = self.client.get('/')
        self.postResp = self.client.post('/', {'nome': ['teste'], 'description': ['descrição do teste']})
        
    def test_200_response(self):
        self.assertEqual(200, self.getResp.status_code)
        
    def test_302_response(self):
        self.assertEqual(302, self.postResp.status_code)
        
    def test_page_title(self):
        self.assertContains(self.getResp, 'Cadastrar Aluno')
        
    def test_template_home(self):
        self.assertTemplateUsed('form.html')
        
        
class faculdadeTest(TestCase):
    def setUp(self):
        self.nome = 'Aluno teste'
        self.professor = 'professorteste', 
        self.register.save()
        
    def test_created(self):
        self.assertTrue(faculdade.objects.exists())
        
    def test_title_task(self):
        nome = self.register.__dict__.get('nome', '')
        self.assertEqual(nome, self.nome)
        
    def test_description_task(self):
        professor = self.register.__dict__.get('professor', '')
        self.assertEqual(professor, self.professor)
        
        
class TaskFormTest(TestCase):
    def test_form_has_fields(self):
        form = TaskForm() 
        expected = ['nome', 'faculdade']
        self.assertSequenceEqual(expected, list(form.fields))