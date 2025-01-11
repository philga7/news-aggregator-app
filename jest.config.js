module.exports = {
    preset: 'ts-jest',
    testEnvironment: 'node',
    moduleNameMapper: {
      '^@/(.*)$': '<rootDir>/app/$1',

    },
    moduleFileExtensions: ['ts', 'tsx', 'js', 'jsx', 'json', 'node'],
    testMatch: ['**/__tests__/**/*.test.[jt]s?(x)'],
    testPathIgnorePatterns: ['/node_modules/', '/tests/'],
    collectCoverageFrom: ['app/**/*.ts', 'app/**/*.tsx'],
  };