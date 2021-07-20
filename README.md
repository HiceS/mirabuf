## Mira 3D Format   

[![npm version](https://badge.fury.io/js/mirabuf.svg)](https://badge.fury.io/js/mirabuf)

Builds:

[![BuildProto](https://github.com/HiceS/mirabuf/actions/workflows/proto_compile.yml/badge.svg)](https://github.com/HiceS/mirabuf/actions/workflows/proto_compile.yml) 

Documentation:

[DOCUMENTATION SITE](https://www.mirabuf.dev/) 

[![GenerateDocs](https://github.com/HiceS/mirabuf/actions/workflows/docs_gen.yml/badge.svg?branch=main)](https://github.com/HiceS/mirabuf/actions/workflows/docs_gen.yml)

Open source file definition for storing, rendering, and translating physical data from generic 3D model assemblies.

You can find build artifacts from the latest build under the Actions Tab

- python
- cpp
- java

Documentation is available as a Build Artifact for now in the GenerateDocs build action.


## Building

#### Build

` protoc -I=. --python_out=./libs/python --java_out=./libs/java --cpp_out=./libs/cpp ./build/mirabuf.proto `

### Build All - Seperate

` protoc -I=. --python_out=./libs/python --java_out=./libs/java --cpp_out=./libs/cpp ./*.proto `

go, c#, swift, rust, node can have additional dependencies

#### Python

` protoc -I=. --python_out=./libs/python ./*.proto `

#### Go

` go install google.golang.org/protobuf/cmd/protoc-gen-go `
` protoc -I=. --go_out=./libs/go ./*.proto ` 

#### Java

` protoc -I=. --java_out=./libs/java ./*.proto `

#### CPP

` protoc -I=. --cpp_out=./libs/cpp ./*.proto `

#### C#

` protoc -I=. --csharp_out=./libs/c# ./*.proto `

#### Swift

` protoc -I=. --swift_out=./libs/swift ./*.proto `

#### Rust

`cargo install protobuf-codegen`

`protoc-gen-rust` -- make sure cargo is in path

`protoc --rust_out ./libs/rust *.proto`

#### Node

To build node you can choose to use the supplied js compiler or use a third party.

I opt to use [protobufjs](https://www.npmjs.com/package/protobufjs) to generate the package and ts bindings.

If you want a zero library implementation you can use the default js_out and rip the build artifact typing.

* Before compiling with this take the time to figure out if commonjs is the right module for you and look over the cli arguments to configure it for however you want to use it. *

` npm i -g protobufjs && mkdir libs/node`

` pbjs -t static-module -w commonjs -o libs/node/mirabuf.js *.proto `

` pbts -o mirabuf.d.ts mirabuf.js `

