import { connect } from 'mongoose';

const uri = 'mongodb://admin:1234qwer@localhost:27017'; // Or change this according to your setup

connect(uri)
  .then(() => {
    console.log('Connected to MongoDB');
  })
  .catch(err => {
    console.error('Error connecting to MongoDB:', err);
  });
