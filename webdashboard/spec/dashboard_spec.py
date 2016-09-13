import json

from main import app
from expects import *



with description('Example App'):
    with before.each:
        self.app = app.test_client()
        self.example = 'example'
        # print dir(self.app)
        # print dir(self.response)
        # print self.response

    with it('has an instance in subject property'):
        expect(self.example).to(equal('example'))
    with it('creates an instance of App'):

        print self.app.application.name
        expect(self.app.application.name).to(equal('dashboard'))
    with context('gets / '):
        with before.each:
            self.response = self.app.get('/')
        with it('is ok'):

            expect(self.response.status_code).to(equal(200))
    with context('gets /static/js/app.js '):
        with before.each:
            self.response = self.app.get('/static/js/app.js')
        with it('is ok'):
            expect(self.response.status_code).to(equal(200))
    with context('gets /json'):
        with before.each:
            self.response = self.app.get('/json')
        with it('is ok'):
            expect(self.response.status_code).to(equal(200))
        with it('returns back foo json'):
            expect(json.loads(self.response.data)).to(equal({ u"sensors": { u"bar": 1 }}))