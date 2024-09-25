import Layout from "./layout";
import Login from "./login";
import Register from "./register/page"

export default function Page() {
  return (
  <Layout>
    <Login></Login>
    <Register></Register>
  </Layout>);
}