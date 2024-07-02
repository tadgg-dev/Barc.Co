import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_guardar_usuario_editado(self):
        form_data = {
            'dni': 'asdasda',
            'usuario': 'adadad',
            'contrasenna': '1231321',
        }
        response = self.app.post('/actualizar/<dni>', data=form_data)
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Invalid input data', response.data)

if __name__ == '__main__':
    unittest.main()