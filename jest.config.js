module.exports = {
    preset: 'ts-jest',
    testEnvironment: 'node',
    moduleNameMapper: {
      '^@/(.*)$': '<rootDir>/app/$1',
    },
    moduleFileExtensions: ['ts', 'tsx', 'js', 'jsx', 'json', 'node'],
    testMatch: ['**/tests/unit/**/*.test.[jt]s?(x)'],
    testPathIgnorePatterns: ['/node_modules/', '/tests/e2e/'],
    collectCoverageFrom: ['app/**/*.ts', 'app/**/*.tsx'],
  };